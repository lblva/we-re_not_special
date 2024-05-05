
// Function to preload images
function preloadImages(imageUrls, callback) {
  let loadedImages = 0;
  let images = [];
  imageUrls.forEach(function(url) {
    console.log('Preloading image: ' + url.src);
    let img = new Image();
    img.onload = function() {
      console.log('Image loaded: ' + url.src);
      loadedImages++;
      if (loadedImages === imageUrls.length) {
        callback(images);
      }
    };
    // Append timestamp to URL to prevent caching
    img.src = url.src + '?timestamp=' + new Date().getTime();
    img.width = 450; // Set desired width
    img.height = 650; // Set desired height
    images.push({ img: img, position: url.position }); // Store image and its position
  });
}

// Function to draw images on the canvas
function drawImages(images) {
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  images.forEach(function(imageData) {
    let img = imageData.img;
    let position = imageData.position;
    ctx.drawImage(img, position.x, position.y, img.width, img.height);
  });
}

// Add image URLs and their fixed positions here
const imagePositions = [
  { src: '/silhouette_1.png', position: { x: 0, y: 120 } },
  { src: '/silhouette_2.png', position: { x: 80, y: 120 } },
  { src: '/silhouette_3.png', position: { x: 150, y: 120 } },
  { src: '/silhouette_4.png', position: { x: 220, y: 120 } },
  { src: '/silhouette_5.png', position: { x: 290, y: 120 } },
  { src: '/silhouette_6.png', position: { x: 360, y: 120 } },
  { src: '/silhouette_7.png', position: { x: 430, y: 120 } },
  { src: '/silhouette_8.png', position: { x: 500, y: 120 } },
  { src: '/silhouette_9.png', position: { x: 570, y: 120 } },
  { src: '/silhouette_10.png', position: { x: 640, y: 120 } },
  { src: '/silhouette_11.png', position: { x: 710, y: 120 } },
  { src: '/silhouette_12.png', position: { x: 790, y: 120 } },
  { src: '/silhouette_12.png', position: { x: 860, y: 120 } },
  { src: '/silhouette_14.png', position: { x: 930, y: 120 } },
  { src: '/silhouette_15.png', position: { x: 1000, y: 120 } },
  { src: '/silhouette_16.png', position: { x: 1070, y: 120 } },
  { src: '/silhouette_17.png', position: { x: 1150, y: 120 } },
  { src: '/silhouette_18.png', position: { x: 1240, y: 120 } },
  { src: '/silhouette_19.png', position: { x: 1320, y: 120 } },
  { src: '/silhouette_20.png', position: { x: 1400, y: 120 } }
  
];

// Set canvas size to match viewport dimensions
const canvas = document.getElementById('canvas');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Preload images before drawing them onto the canvas
setInterval(()=> {
  console.log('Preloading images...');
  preloadImages(imagePositions, function(images) {
    drawImages(images);
    console.log('Images loaded and drawn');
    
  })
}, 5000)

