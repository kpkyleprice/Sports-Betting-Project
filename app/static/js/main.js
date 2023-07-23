  let slideIndex = 0;
  showSlides();
  
  function showSlides() {
    let i;
    let slides = document.getElementsByClassName("carousel-item");
    let dots = document.getElementsByClassName("carousel-indicators")[0].getElementsByTagName("li");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {
      slideIndex = 1;
    }
    slides[slideIndex-1].style.display = "block";
    for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
    }
    dots[slideIndex-1].className += " active";
    setTimeout(showSlides, 5000); // Change image every 5 seconds
  }

  window.addEventListener('scroll', function() {
    var pageTitle = document.getElementById('header');
    var scrollPosition = window.scrollY;
    var pageTitlePosition = pageTitle.getBoundingClientRect().top;
    if (scrollPosition > pageTitlePosition + window.innerHeight * 0.5) {
      pageTitle.classList.add('visible');
    } else {
      pageTitle.classList.remove('visible');
    }
  });

  