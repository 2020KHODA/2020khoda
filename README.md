<!DOCTYPE html>
<html lang="fa">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>2020KHODA - املاک انحصاری</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');

  body {
    margin: 0;
    font-family: 'Tahoma', sans-serif;
    background: radial-gradient(circle at top, #0d0d0d, #000);
    color: #fff;
    overflow-x: hidden;
    perspective: 1000px;
  }

  header {
    text-align: center;
    padding: 100px 20px;
    font-family: 'Orbitron', sans-serif;
    font-size: 4rem;
    color: #ffcc00;
    text-shadow:
      0 0 10px #ffcc00,
      0 0 20px #ff9900,
      0 0 30px #ff6600;
    animation: glow 2s ease-in-out infinite alternate;
  }

  @keyframes glow {
    0% { text-shadow: 0 0 5px #ffcc00, 0 0 10px #ff9900; }
    100% { text-shadow: 0 0 20px #ffcc00, 0 0 40px #ff9900, 0 0 60px #ff6600; }
  }

  .property-card {
    max-width: 700px;
    margin: 50px auto;
    background: rgba(255, 255, 255, 0.05);
    border: 2px solid #ffcc00;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 0 30px #ffcc00;
    transition: transform 0.3s, box-shadow 0.3s;
  }

  .property-card img {
    width: 100%;
    display: block;
    border-bottom: 2px solid #ffcc00;
    transform-origin: center;
    transition: transform 0.3s;
  }

  .property-info {
    padding: 25px 30px;
  }

  .property-info h2 {
    font-size: 2.5rem;
    margin-bottom: 15px;
    color: #ffcc00;
    text-shadow: 0 0 10px #ffcc00;
  }

  .property-info p {
    font-size: 1.2rem;
    line-height: 1.6;
  }

  .buy-btn {
    display: block;
    width: 80%;
    margin: 25px auto 50px auto;
    padding: 18px;
    text-align: center;
    background: linear-gradient(45deg, #ffcc00, #ff9900);
    color: #000;
    font-weight: bold;
    font-size: 1.3rem;
    border: none;
    border-radius: 15px;
    cursor: pointer;
    text-decoration: none;
    transition: transform 0.3s, box-shadow 0.3s;
  }

  .buy-btn:hover {
    transform: scale(1.1);
    box-shadow: 0 0 30px #ffcc00;
  }

  .stars {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: transparent;
    z-index: 0;
    pointer-events: none;
  }

  .star {
    position: absolute;
    width: 2px; height: 2px;
    background: white;
    border-radius: 50%;
    animation: twinkle 2s infinite alternate;
  }

  @keyframes twinkle {
    0% { opacity: 0.3; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.5); }
    100% { opacity: 0.3; transform: scale(1); }
  }
</style>
</head>
<body>

<header>2020KHODA</header>

<div class="property-card" id="propertyCard">
  <img src="https://via.placeholder.com/700x400" alt="ملک ۲۰هزارمتری" id="propertyImg">
  <div class="property-info">
    <h2>ملک ۲۰هزارمتری الماس‌گونه</h2>
    <p>این ملک بی‌نظیر با لوکیشنی استراتژیک، طراحی خیره‌کننده و انحصاری، برای کسانی که به دنبال قدرت و جاودانگی هستند.</p>
    <p>ویژگی‌ها: ۲۰هزار متر مربع، دسترسی عالی، محیطی خاص و سرمایه‌گذاری منحصر به فرد.</p>
  </div>
  <a href="#" class="buy-btn">تماس برای خرید</a>
</div>

<div class="stars" id="stars"></div>

<script>
  // ستاره‌های پس‌زمینه
  const starsContainer = document.getElementById('stars');
  for (let i = 0; i < 150; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    star.style.top = Math.random() * window.innerHeight + 'px';
    star.style.left = Math.random() * window.innerWidth + 'px';
    star.style.animationDuration = (1 + Math.random() * 3) + 's';
    star.style.width = star.style.height = (1 + Math.random() * 2) + 'px';
    starsContainer.appendChild(star);
  }

  // افکت 3D روی کارت ملک با حرکت موس
  const card = document.getElementById('propertyCard');
  const img = document.getElementById('propertyImg');
  card.addEventListener('mousemove', e => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width/2;
    const y = e.clientY - rect.top - rect.height/2;
    card.style.transform = `rotateY(${x/20}deg) rotateX(${-y/20}deg) scale(1.05)`;
    img.style.transform = `translateZ(20px)`;
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = 'rotateY(0deg) rotateX(0deg) scale(1)';
    img.style.transform = 'translateZ(0)';
  });
</script>

</body>
</html>