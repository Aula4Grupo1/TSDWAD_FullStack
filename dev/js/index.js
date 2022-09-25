$('#myModal').on('show.bs.modal', function () {
    $('.modal-content').css('max-height',$( window ).height()*0.8);
    $('.modal-content img').css('max-height',(($( window ).height()*0.8)-86));
    });