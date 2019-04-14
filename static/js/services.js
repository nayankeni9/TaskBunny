var $select1 = $( '#select1' ),
$select2 = $( '#select2' ),
$options = $select2.find( 'option' );

$select1.on( 'change', function() {
$select2.html( $options.filter( '[value="' + this.value + '"]' ) );
} ).trigger( 'change' );

// function paginate(){
//     document.getElementById("previous").style.display="none";
//     document.getElementById("next").style.display="block";
    
// };
function pagechange(frompage, topage) {
    var page=document.getElementById('formpage_'+frompage);
    if (!page) return false;
    page.style.visibility='hidden';
    page.style.display='none';
  
    page=document.getElementById('formpage_'+topage);
    if (!page) return false;
    page.style.display='block';
    page.style.visibility='visible';
  
    return true;
  }