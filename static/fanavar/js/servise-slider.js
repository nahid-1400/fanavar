const wrapper = document.querySelector(".wrapper");
const carousel = document.querySelector(".carousel");
const firstCardWidth = carousel.querySelector(".card").offsetWidth;
const arrowBtns = document.querySelectorAll(".wrapper i");
const carouselChildrens = [...carousel.children];
let isDragging = false, isAutoPlay = true, startX, startScrollLeft, timeoutId;



// Get the number of cards that can fit in the carousel at once
// تعداد کارت‌هایی را که می‌توانند در چرخ فلک قرار بگیرند به‌طور هم‌زمان دریافت میکند

let cardPerView = Math.round(carousel.offsetWidth / firstCardWidth);



// Insert copies of the last few cards to beginning of carousel for infinite scrolling
// کپی چند کارت آخر را برای پیمایش بی نهایت در ابتدای چرخ فلک قرار میدهد

carouselChildrens.slice(-cardPerView).reverse().forEach(card => {
    carousel.insertAdjacentHTML("afterbegin", card.outerHTML);
});



// Insert copies of the first few cards to end of carousel for infinite scrolling
// برای پیمایش بی نهایت، کپی چند کارت اول را در انتهای چرخ فلک قرار میدهد

carouselChildrens.slice(0, cardPerView).forEach(card => {
    carousel.insertAdjacentHTML("beforeend", card.outerHTML);
});



// Scroll the carousel at appropriate postition to hide first few duplicate cards on Firefox
// چرخ فلک را در موقعیت مناسب اسکرول میکند تا اولین کارت های تکراری را در فایرفاکس مخفی کند

carousel.classList.add("no-transition");
carousel.scrollLeft = carousel.offsetWidth;
carousel.classList.remove("no-transition");


// Add event listeners for the arrow buttons to scroll the carousel left and right
// برای پیمایش چرخ و فلک به چپ و راست

arrowBtns.forEach(btn => {
    btn.addEventListener("click", () => {
        carousel.scrollLeft += btn.id == "left" ? -firstCardWidth : firstCardWidth;
    });
});
const dragStart = (e) => {
    isDragging = true;
    carousel.classList.add("dragging");



    // Records the initial cursor and scroll position of the carousel
    // مکان نما و موقعیت اسکرول اولیه چرخ فلک را ثبت می کند

    startX = e.pageX;
    startScrollLeft = carousel.scrollLeft;
}
const dragging = (e) => {
    if (!isDragging) return;


    // if isDragging is false return from here Updates the scroll position of the carousel based on the cursor movement
    // موقعیت اسکرول چرخ فلک را بر اساس حرکت مکان نما به روز می کند

    carousel.scrollLeft = startScrollLeft - (e.pageX - startX);
}
const dragStop = () => {
    isDragging = false;
    carousel.classList.remove("dragging");
}
const infiniteScroll = () => {

    // If the carousel is at the beginning, scroll to the end
    // اگر چرخ فلک در ابتدا است، به انتها بروید

    if (carousel.scrollLeft === 0) {
        carousel.classList.add("no-transition");
        carousel.scrollLeft = carousel.scrollWidth - (2 * carousel.offsetWidth);
        carousel.classList.remove("no-transition");
    }
    // If the carousel is at the end, scroll to the beginning
    // اگر چرخ فلک در انتها است، به ابتدا بروید

    else if (Math.ceil(carousel.scrollLeft) === carousel.scrollWidth - carousel.offsetWidth) {
        carousel.classList.add("no-transition");
        carousel.scrollLeft = carousel.offsetWidth;
        carousel.classList.remove("no-transition");
    }

    // Clear existing timeout & start autoplay if mouse is not hovering over carousel
    // مهلت زمانی موجود را برسی کن و اگر ماوس روی چرخ فلک قرار نگرفت، پخش خودکار را شروع کن

    clearTimeout(timeoutId);
    if (!wrapper.matches(":hover")) autoPlay();
}
const autoPlay = () => {
    if (window.innerWidth < 800 || !isAutoPlay) return; // Return if window is smaller than 800 or isAutoPlay is false

    // Autoplay the carousel after every 2500 ms
    timeoutId = setTimeout(() => carousel.scrollLeft += firstCardWidth, 2500);
}
autoPlay();
carousel.addEventListener("mousedown", dragStart);
carousel.addEventListener("mousemove", dragging);
document.addEventListener("mouseup", dragStop);
carousel.addEventListener("scroll", infiniteScroll);
wrapper.addEventListener("mouseenter", () => clearTimeout(timeoutId));
wrapper.addEventListener("mouseleave", autoPlay);