window.addEvent('domready', function(){
       {
                var count = 0;
                $('box').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
                        }
                });
                $('chk').set('text',count);
        });
});

        $('count-button').addEvent('click', function(){
                var count = 0;
                $('box2').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
                        }
                });
                   $('chk').set('text',count);
        });
});

        $('count-button').addEvent('click', function(){
                var count = 0;
                $('box3').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
                        }
                });
                    $('chk').set('text',count);
        });
});
{
        $('count-button').addEvent('click', function(){
                var count = 0;
                $('box4').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
                        }
                });
                     $('chk').set('text',count);
        });
});

