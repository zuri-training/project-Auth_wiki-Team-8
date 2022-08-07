const faqs = document.querySelectorAll(".faqs");

faqs.forEach(faq => {
    faq.addEventListener("click", () => {
        faq.classList.toggle("access");
    });
});