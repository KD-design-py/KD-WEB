document.addEventListener('DOMContentLoaded', function () {
    const videos = document.querySelectorAll('.fade-in-video');

    function fadeInVideos() {
        videos.forEach(video => {
            video.classList.add('visible');
        });
    }

    setTimeout(fadeInVideos, 2000); // Fade in after 2 seconds
});