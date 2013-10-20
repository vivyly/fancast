var Overlay = (function(){
    current_status = false,
    overlay_base = null,
    init = function(){
        console.log('INIT');
        $('#dialog').dialog({
            autoOpen:false,
            modal:true,
            show:"blind",
            hide:"blind"
        });
    },
    show = function(){ 
        console.log('SHOW');
        $('#dialog').dialog("open");
        return false;
    },
    close = function(){
        $('#dialog').dialog("close");
        return false;
    };

    return {
        init: init,
        show: show,
        close: close
    };
})();
