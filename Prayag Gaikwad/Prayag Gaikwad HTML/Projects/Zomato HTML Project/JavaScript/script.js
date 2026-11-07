const restaurantCards = document.querySelectorAll('.restaurant-card');
const menuToggle = document.querySelector('.menu-toggle');
const mainNav = document.querySelector('.main-nav');

document.querySelector('#search-form').addEventListener('submit', function (event) {
	event.preventDefault();
	const query = document.querySelector('#dish-input').value.trim().toLowerCase();
	restaurantCards.forEach(function (card) {
		card.hidden = query && !card.textContent.toLowerCase().includes(query);
	});
	document.querySelector('#restaurants').scrollIntoView({ behavior: 'smooth' });
});

document.querySelectorAll('.filter-tabs button').forEach(function (button) {
	button.addEventListener('click', function () {
		document.querySelector('.filter-tabs button.active').classList.remove('active');
		button.classList.add('active');
		const filter = button.dataset.filter;
		restaurantCards.forEach(function (card) {
			card.hidden = filter !== 'all' && card.dataset.category !== filter;
		});
	});
});

document.querySelectorAll('.heart').forEach(function (button) {
	button.addEventListener('click', function () {
		button.classList.toggle('saved');
		button.textContent = button.classList.contains('saved') ? '\u2665' : '\u2661';
	});
});

menuToggle.addEventListener('click', function () {
	const isOpen = mainNav.classList.toggle('open');
	menuToggle.setAttribute('aria-expanded', isOpen);
});
n