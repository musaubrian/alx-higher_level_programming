let skywarsData = []
var skywars = async function(){
    await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
    .then((response) => response.json())
    .then((data) => (skywarsData = data))

    $("#character").text(skywarsData.name);
}

skywars()