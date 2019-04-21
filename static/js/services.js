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

function getTaskerList(){
  var tasker_list;
  var category = document.getElementById("select1").value;
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      tasker_list = JSON.parse(this.responseText);
    }
  };
  xmlHttp.open("GET", "/tasker_list?category="+category, false); // true for asynchronous
  xmlHttp.send(null);
  createTaskers(tasker_list);
  return pagechange(1,2);
}


function createTaskers(tasker_list){
  var element = document.getElementById("tasker_list");
  let ele = ''
  for(let i=0;i<tasker_list.tasker_list.length;i++){
    ele +='<div class="col-md-4 wow fadeInUp"><div class="about-col"><div class="img"><img src="'+tasker_list.tasker_list[i].image+'" alt="" class="img-fluid">    </div><h2 class="title"><a href="#">'+tasker_list.tasker_list[i].firstname+' '+tasker_list.tasker_list[i].lastname+'</a></h2><p>"'+tasker_list.tasker_list[i].about_me+'"</p><p>Age: '+tasker_list.tasker_list[i].tasker_age+' <br/><span>Rating: 3/5</span><br/><span id="service_rate">Service Rate:'+tasker_list.tasker_list[i].service_rate+' $/hr</span><br/><input id="emailid" value="'+tasker_list.tasker_list[i].email+'" type="hidden"></p><button type="button" class="btn btn-lg btn-warning" style="width: 100%; bottom: 0;" onclick="selectTasker(this.id)" id="'+tasker_list.tasker_list[i].id+'">Select</button></div></div>';
  }
  if(ele==''){
    ele = 'No Tasker found'
  }
  element.innerHTML =ele
}

function selectTasker(id){
  var emailid = document.getElementById(id).parentNode.querySelector("input").value;
  console.log(emailid)
  var name = document.getElementById(id).parentNode.childNodes[1].querySelector("h2 a").text;
  var e1 = document.getElementById("select1");
  var category = e1.options[e1.selectedIndex].text;
  var e2 = document.getElementById("select2");
  var subcategory = e2.options[e2.selectedIndex].text;
  var date = document.getElementsByName("date")[0].value;
  var time = document.getElementsByName("time")[0].value+":00";
  var e3 = document.getElementById("select3");
  var location = e3.options[e3.selectedIndex].text;
  var address = document.getElementsByName("address")[0].value;
  var spantext = document.getElementById("service_rate").innerHTML;
  var service_rate = spantext.substring(spantext.indexOf(':')+1, spantext.indexOf('$')-1)
  var service_description = document.getElementById("service_description").value

  document.getElementById("preview_service").value= category;
  document.getElementById("preview_service_type").value= subcategory;
  document.getElementById("preview_date").value= date;
  document.getElementById("preview_time").value= time;
  document.getElementById("preview_location").value= location;
  document.getElementById("preview_address").value= address;
  document.getElementById("preview_tasker_name").value= name;
  document.getElementById("preview_tasker_email").value= emailid;
  document.getElementById("preview_rate").value= service_rate;
  document.getElementById("preview_description").value= service_description;
  
  return pagechange(2,3);
}