var Overlay = (function(){
    Overlay = {};
    Overlay.open_status = false;
    Overlay.open_form = '';
    Overlay.init = function(){
        $('#dialog').dialog({
            autoOpen:false,
            modal:true,
            show:"blind",
            hide:"blind"
        });
    },
    Overlay.close = function(){
        $('#dialog').dialog("close");
        $(Overlay.open_form).addClass('hidden');
        Overlay.open_status = false;
        return false;
    },
    Overlay.show = function(open_form){ 
        if (Overlay.open_status)
            Overlay.close();
        Overlay.open_form = open_form;
        $(Overlay.open_form).removeClass('hidden');
        $('#dialog').dialog("open");
        Overlay.open_status = true;
        return false;
    };
    
    return Overlay;
})();
