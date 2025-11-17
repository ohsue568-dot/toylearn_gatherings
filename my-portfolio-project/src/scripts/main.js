// main.js

// 스크립트가 성공적으로 로드되었는지 확인
console.log("Script loaded!");

// 여기에 GSAP 또는 Framer Motion과 같은 애니메이션 라이브러리 코드를 추가할 수 있습니다.
// 예: 스크롤 트리거 애니메이션, 인터랙티브 요소 등

document.addEventListener('DOMContentLoaded', () => {
    // 부드러운 스크롤 구현
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
