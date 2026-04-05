// Hebt Kündigungs-Buttons auf der Apple-Seite hervor
function highlightCancelButtons() {
  const buttons = document.querySelectorAll("button, a");
  buttons.forEach((el) => {
    const text = el.textContent.toLowerCase();
    if (
      text.includes("cancel") ||
      text.includes("kündigen") ||
      text.includes("beenden")
    ) {
      el.style.outline = "3px solid #ff3b30";
      el.style.outlineOffset = "3px";
      el.style.borderRadius = "4px";
    }
  });
}

// Warte bis die Seite geladen ist, dann hervorheben
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", highlightCancelButtons);
} else {
  highlightCancelButtons();
}

// Beobachte dynamische Änderungen (SPA)
const observer = new MutationObserver(highlightCancelButtons);
observer.observe(document.body, { childList: true, subtree: true });
