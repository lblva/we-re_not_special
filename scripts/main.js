
// Function to preload images
function preloadImages(imageUrls, callback) {
  let loadedImages = 0;
  let images = [];
  imageUrls.forEach(function(url) {
    let img = new Image();
    img.onload = function() {
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
  { src: '/silhouette_1.png', position: { x: 5, y: 120 } },
  { src: '/silhouette_2.png', position: { x: 90, y: 120 } },
  { src: '/silhouette_3.png', position: { x: 180, y: 120 } },
  { src: '/silhouette_4.png', position: { x: 260, y: 120 } },
  { src: '/silhouette_5.png', position: { x: 340, y: 120 } },
  { src: '/silhouette_6.png', position: { x: 420, y: 120 } },
  { src: '/silhouette_7.png', position: { x: 500, y: 120 } },
  { src: '/silhouette_8.png', position: { x: 580, y: 120 } },
  { src: '/silhouette_9.png', position: { x: 660, y: 120 } },
  { src: '/silhouette_10.png', position: { x: 740, y: 120 } },
  { src: '/silhouette_11.png', position: { x: 820, y: 120 } },
  { src: '/silhouette_12.png', position: { x: 880, y: 120 } },
  { src: '/silhouette_12.png', position: { x: 960, y: 120 } },
  { src: '/silhouette_14.png', position: { x: 1020, y: 120 } },
  { src: '/silhouette_15.png', position: { x: 1100, y: 120 } },
  { src: '/silhouette_16.png', position: { x: 1150, y: 120 } },
  { src: '/silhouette_17.png', position: { x: 1210, y: 120 } },
  { src: '/silhouette_18.png', position: { x: 1380, y: 120 } },
  { src: '/silhouette_19.png', position: { x: 1440, y: 120 } },
  { src: '/silhouette_20.png', position: { x: 1550, y: 120 } }
];

// Set canvas size to match viewport dimensions
const canvas = document.getElementById('canvas');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Preload images before drawing them onto the canvas
setInterval(()=> {
  preloadImages(imagePositions, function(images) {
    drawImages(images);
    
  })
}, 5000)
