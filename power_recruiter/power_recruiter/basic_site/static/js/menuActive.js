$(function() {
    if (window.location.pathname.substring(1).indexOf("Chart") > -1) {
        $(".statsli").addClass('active');
    }
    else {
        $(".homeli").addClass('active');
    }
});