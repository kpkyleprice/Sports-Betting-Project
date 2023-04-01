// const options = {
// 	method: 'GET',
// 	headers: {
// 		'X-RapidAPI-Key': 'ec69f279f2msh0dce01f04649adfp134d99jsn6168c4818231',
// 		'X-RapidAPI-Host': 'odds.p.rapidapi.com'
// 	}
// };


// fetch('https://odds.p.rapidapi.com/v4/sports/basketball_ncaab/odds?regions=us&oddsFormat=american&markets=h2h', options)
// .then((response) => {
//     if (response.ok) {
//       return response.json();
//     } else {
//       throw new Error("NETWORK RESPONSE ERROR");
//     }
//   })
//   .then(data => {
//     console.log(data);
//     displayGame(data)
//   })
//   .catch((error) => console.error("FETCH ERROR:", error));


    function displayGame(data) {
    for (let i = 0; i < 6; i++) {
      const game = data[`${i}`];
      const infoDiv = document.getElementById(`info${i}`); 
      console.log(infoDiv)
      const MatchupName = (game.home_team + "  vs  " + game.away_team);
      const heading = document.createElement("h2");
      heading.innerHTML = MatchupName;
      infoDiv.appendChild(heading);
  
      const getOdds = game.bookmakers[0].markets[0].outcomes
      const spread = Object.values(getOdds);
      const HomeOdds = document.createElement("ul");
      const AwayOdds = document.createElement("ul");
      HomeOdds.innerHTML = (spread[0].name + "  " + spread[0].price);
      AwayOdds.innerHTML = (spread[1].name + "  " + spread[1].price);
      infoDiv.appendChild(HomeOdds)
      infoDiv.appendChild(AwayOdds)
    }


  }
// home page
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