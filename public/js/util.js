cramsanHelper = {
  goToUrl: function(url) {
    setTimeout(function() { window.location = url; }, 500); 
  },
};

function setDrawerToNarrow(){
  var drawerPanel = document.getElementById('drawerpanel');
  var drawerContent = document.getElementById('drawercontent');
  var drawerContentShadow = document.getElementById('drawercontent-shadow');
  drawerContentShadow.className = "drawercontent-shadow-narrow";
  drawerContentShadow.setZ(0);
  drawerContent.className = "drawercontent-narrow"
}

function setDrawerToWide(){
  var drawerPanel = document.getElementById('drawerpanel');
  var drawerContent = document.getElementById('drawercontent');
  var drawerContentShadow = document.getElementById('drawercontent-shadow');
  drawerContentShadow.className = "drawercontent-shadow-wide";
  drawerContentShadow.setZ(1);
  drawerContent.className = "drawercontent-wide"
}

function setDrawerNarrowMode(narrow){
    if(narrow){
      setDrawerToNarrow();
    } else {
      setDrawerToWide();
    }
}
document.addEventListener('polymer-ready', function() {
  var navicon = document.getElementById('navicon');
  var drawerPanel = document.getElementById('drawerpanel');    
  navicon.addEventListener('click', function() {
    drawerPanel.togglePanel();
    setDrawerNarrowMode(drawerPanel.narrow);
  });
});

document.addEventListener('core-responsive-change', function(event) {
  setDrawerNarrowMode(event.detail.narrow);
});

window.onload = function () {
  var drawerPanel = document.getElementById('drawerpanel');    
  setDrawerNarrowMode(drawerPanel.narrow);
}