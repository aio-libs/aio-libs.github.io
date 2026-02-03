const template = document.getElementById("template-sponsor-sidebar");
const sponsors = JSON.parse(template.dataset.sponsors);
const sponsor = sponsors[Math.floor(Math.random() * sponsors.length)];

const clone = document.importNode(template.content, true);
clone.querySelector("a").href = sponsor.url;
const img = clone.querySelector("img");
img.src = sponsor.img;
img.alt = sponsor.name;

document.getElementById("sponsor-sidebar").appendChild(clone);
