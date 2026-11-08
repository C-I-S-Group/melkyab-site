
document.addEventListener("DOMContentLoaded", function () {
    const page = document.documentElement;
    const themeButtons = document.querySelectorAll(".theme-toggle");
    const menuButton = document.querySelector(".menu-toggle");
    const mainNav = document.querySelector(".main-nav");


    let savedTheme = null;
    try {
        savedTheme = localStorage.getItem("cis-theme");
    } catch (error) {

    }

    if (savedTheme === "dark" || savedTheme === "light") {
        page.setAttribute("data-theme", savedTheme);
    }

    function updateThemeButtons() {
        const isDark = page.getAttribute("data-theme") === "dark";
        themeButtons.forEach(function (button) {
            button.textContent = isDark ? "☀" : "☾";
            button.setAttribute("aria-label", isDark ? "فعال کردن حالت روشن" : "فعال کردن حالت تاریک");
            button.setAttribute("title", isDark ? "حالت روشن" : "حالت تاریک");
            button.setAttribute("aria-pressed", String(isDark));
        });
    }

    updateThemeButtons();

    themeButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const nextTheme = page.getAttribute("data-theme") === "dark" ? "light" : "dark";
            page.setAttribute("data-theme", nextTheme);
            try {
                localStorage.setItem("cis-theme", nextTheme);
            } catch (error) {
                // The theme still changes for the current page if storage is unavailable.
            }
            updateThemeButtons();
        });
    });


    if (menuButton && mainNav) {
        menuButton.addEventListener("click", function () {
            const isOpen = mainNav.classList.toggle("open");
            menuButton.setAttribute("aria-expanded", String(isOpen));
            menuButton.setAttribute("aria-label", isOpen ? "بستن منو" : "باز کردن منو");
            menuButton.textContent = isOpen ? "×" : "☰";
        });
    }


    const propertyCards = Array.from(document.querySelectorAll(".property-card"));
    const searchForm = document.querySelector("#propertySearchForm");
    const searchInput = document.querySelector("#propertySearch");
    const neighborhoodSelect = document.querySelector("#neighborhoodFilter");
    const typeSelect = document.querySelector("#typeFilter");
    const filterButtons = document.querySelectorAll(".filter-btn");
    const resultCount = document.querySelector("#resultCount");
    const noResults = document.querySelector("#noResults");
    const isSearchPreview = !!(searchForm && searchForm.dataset.previewMode === "true");

    function normalizeText(value) {
        return String(value || "")
            .toLocaleLowerCase("fa-IR")
            .replace(/[يى]/g, "ی")
            .replace(/ك/g, "ک")
            .replace(/[۰-۹]/g, function (digit) { return String("۰۱۲۳۴۵۶۷۸۹".indexOf(digit)); })
            .replace(/[٠-٩]/g, function (digit) { return String("٠١٢٣٤٥٦٧٨٩".indexOf(digit)); })
            .trim();
    }

    function filterPreviewProperties() {
        if (!isSearchPreview || !propertyCards.length) return;

        const query = normalizeText(searchInput ? searchInput.value : "");
        const neighborhood = neighborhoodSelect ? neighborhoodSelect.value : "";
        const chosenType = typeSelect ? typeSelect.value : "";
        let visibleCount = 0;

        propertyCards.forEach(function (card) {
            const cardText = normalizeText(card.textContent);
            const matchesText = !query || cardText.includes(query);
            const matchesNeighborhood = !neighborhood || neighborhood === card.dataset.neighborhood;
            const matchesType = !chosenType || chosenType === card.dataset.type;
            const shouldShow = matchesText && matchesNeighborhood && matchesType;

            card.hidden = !shouldShow;
            if (shouldShow) visibleCount += 1;
        });

        if (resultCount) resultCount.textContent = visibleCount.toLocaleString("fa-IR") + " ملک";
        if (noResults) noResults.hidden = visibleCount !== 0;
    }

    if (isSearchPreview) {
        if (searchInput) searchInput.addEventListener("input", filterPreviewProperties);
        if (neighborhoodSelect) neighborhoodSelect.addEventListener("change", filterPreviewProperties);
        if (searchForm) {
            searchForm.addEventListener("submit", function (event) {
                event.preventDefault();
                filterPreviewProperties();
                const propertiesSection = document.querySelector("#properties");
                if (propertiesSection) propertiesSection.scrollIntoView({ behavior: "smooth", block: "start" });
            });
        }


        if (searchInput) {
            const params = new URLSearchParams(window.location.search);
            const incomingQuery = params.get("q");
            const incomingNeighborhood = params.get("neighborhood");
            const incomingType = params.get("property_type");
            if (incomingQuery) searchInput.value = incomingQuery;
            if (incomingNeighborhood && neighborhoodSelect) neighborhoodSelect.value = incomingNeighborhood;
            if (incomingType && typeSelect) typeSelect.value = incomingType;
            if (incomingQuery || incomingNeighborhood || incomingType) filterPreviewProperties();
        }
    }


    if (typeSelect) {
        typeSelect.addEventListener("change", function () {
            filterButtons.forEach(function (button) {
                const filterValue = button.dataset.filter === "all" ? "" : (button.dataset.filter || "");
                button.classList.toggle("active", filterValue === typeSelect.value);
            });
            if (isSearchPreview) filterPreviewProperties();
        });
    }

    filterButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const filterValue = button.dataset.filter === "all" ? "" : (button.dataset.filter || "");
            if (typeSelect) typeSelect.value = filterValue;
            filterButtons.forEach(function (item) { item.classList.toggle("active", item === button); });

            if (isSearchPreview) {
                filterPreviewProperties();
            } else if (searchForm) {
                if (typeof searchForm.requestSubmit === "function") {
                    searchForm.requestSubmit();
                } else {
                    searchForm.submit();
                }
            }
        });
    });


    document.querySelectorAll(".header-search.site-search[data-preview-mode='true']").forEach(function (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            const field = form.querySelector("input[name='q']");
            const query = field ? field.value.trim() : "";
            const homeSearch = document.querySelector("#propertySearchForm");

            if (homeSearch && homeSearch.dataset.previewMode === "true") {
                if (searchInput) searchInput.value = query;
                filterPreviewProperties();
                const propertiesSection = document.querySelector("#properties");
                if (propertiesSection) propertiesSection.scrollIntoView({ behavior: "smooth", block: "start" });
            } else {
                window.location.href = "index.html?q=" + encodeURIComponent(query) + "#properties";
            }
        });
    });


    const contactForm = document.querySelector("#contactForm");
    const formMessage = document.querySelector("#formMessage");
    if (contactForm && contactForm.dataset.previewMode === "true" && formMessage) {
        contactForm.addEventListener("submit", function (event) {
            event.preventDefault();
            if (!contactForm.reportValidity()) return;
            formMessage.hidden = false;
            formMessage.textContent = "این نسخه فقط پیش‌نمایش فرانت‌اند است؛ اطلاعات شما ارسال یا ذخیره نشد. پس از اتصال بک‌اند، ثبت درخواست فعال می‌شود.";
        });
    }


    const propertySlugInput = document.querySelector("#propertySlug");
    if (propertySlugInput) {
        const params = new URLSearchParams(window.location.search);
        const propertySlug = params.get("property");
        const requestType = params.get("request_type");
        if (propertySlug) propertySlugInput.value = propertySlug;
        const subjectSelect = document.querySelector("#subject");
        if (requestType && subjectSelect) subjectSelect.value = requestType;
    }

    // Footer year.
    document.querySelectorAll("[data-year]").forEach(function (item) {
        item.textContent = new Date().getFullYear().toLocaleString("fa-IR");
    });
});
