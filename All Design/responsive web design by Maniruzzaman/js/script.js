// Typing Script JS
var typed = new Typed(".typing",{
    strings: ["Python Developer","Web Developer(Django)", "Youtuber", "Blogger"],
    typeSpeed: 80,
    backSpeed: 80,
});

var typed = new Typed(".typing-2",{
    strings: ["Python Developer","Web Developer(Django)", "Web Designer", "Youtuber", "Blogger"],
    typeSpeed: 100,
    backSpeed: 60,
});

// Show/Hide FAQs answer
const faqs = document.querySelectorAll('.faq');
faqs.forEach(faq => {
    faq.addEventListener('click', () => {
        faq.classList.toggle('open');

        //change icon
        const icon = faq.querySelector('.faq_icon i');
        if (icon.className === 'fa-solid fa-plus'){
            icon.className = 'fa-solid fa-minus';
        }
        else{
            icon.className = 'fa-solid fa-plus';
        }

    })
})

//Show/hide nav menu
const menu = document.querySelector('.nav_menu');
const menuBtn = document.querySelector('#open-menu-btn');
const closeBtn = document.querySelector('#close-menu-btn');

menuBtn.addEventListener('click', () => {
    menu.style.display = "flex";
    closeBtn.style.display = "inline-block";
    menuBtn.style.display = "none";
})

//close nav menu
const closeNav = () => {
    menu.style.display = "none";
    closeBtn.style.display = "none";
    menuBtn.style.display = "inline-block";
}
closeBtn.addEventListener('click', closeNav);

//nav color change on scroll
window.addEventListener('scroll', () => {
    document.querySelector('nav').classList.toggle('window-scroll', window.scrollY>100);
})

// console.log($('.see_sec1').length)
//   console.log("yes", $('.main_div1').length)

//   $('.see_sec1').each(function (i) {
//     console.log("index", i)
//     current = $(this)

//     $(current).click(function () {
//       alert("asdasdsadasd")
//       console.log(i)
//       $('.main_div1').removeClass('x2')
//       $('.main_div1').addClass('dobble_inner_text')
//       $('.main_div1:eq(' + i + ')').removeClass('dobble_inner_text')
//       $('.main_div1:eq(' + i + ')').addClass('x2')

//       // $(this).addClass('x2')
//     })

//   });