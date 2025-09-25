function toggleReadMore() {
  const moreText = document.getElementById("more");
  const btn = document.getElementById("readMoreBtn");

  if (moreText.style.display === "none") {
    moreText.style.display = "inline";
    btn.innerText = "Show less";
  } else {
    moreText.style.display = "none";
    btn.innerText = "Read more";
  }
}