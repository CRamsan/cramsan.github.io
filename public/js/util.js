cramsanHelper = {
  goToUrl: function(url) {
    setTimeout(function() { window.location = url; }, 500); 
  },
  shareCurrentPageToUrl: function(shareUrl) {
    var externalUrl = shareUrl + encodeURIComponent(window.location);
    window.location = externalUrl;
  },

};

function w3_open() {
    document.getElementsByClassName("w3-sidenav")[0].style.display = "block";
}
function w3_close() {
    document.getElementsByClassName("w3-sidenav")[0].style.display = "none";
}
