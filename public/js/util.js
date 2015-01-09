cramsanHelper = {
  goToUrl: function(url) {
    setTimeout(function() { window.location = url; }, 500); 
  },
};

document.addEventListener('polymer-ready', function() {
  var navicon = document.getElementById('navicon');
  var drawerPanel = document.getElementById('drawerpanel');
  navicon.addEventListener('click', function() {
    drawerPanel.togglePanel();
  });
});
