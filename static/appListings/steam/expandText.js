function toggleSeeMore() {
    if(document.getElementById("textarea").style.display == 'none') {
        document.getElementById("textarea").style.display = 'block';
        document.getElementById("seeMore").innerHTML = 'See less';
    }
    else {
        document.getElementById("textarea").style.display = 'none';
        document.getElementById("seeMore").innerHTML = 'See more';        
    }
}