document.getElementById("openApple").addEventListener("click", () => {
  chrome.tabs.create({
    url: "https://appleid.apple.com/account/manage/section/subscriptions"
  });
  window.close();
});
