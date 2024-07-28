
document.write('<head></head><body>');
document.write('<div id="top2" style="display:inline-block;border:0px solid red;padding-bottom:7px"></div><br>')
document.write('<div class="titles" id="top1" style="display:inline-block;border:0px solid blue;padding-bottom:3px"></div><br>')
document.write('<div id="top" style="display:inline-block;border: 0px solid red; padding-bottom:3px"></div><br>');
document.write('<div id="sub_top" style="display:inline-block;border: 0px solid red; padding-bottom:7px"></div>');


var m0=['home','OOFe','Okean','How to'];

if (here0=='home'){
  var m1=['home.html','./oofe/index.html','./okean/index.html','./howto/index.html'];
  $('head').append('<link rel="stylesheet" href="./file.css">');
}else{
  var m1=['../home.html','../oofe/index.html','../okean/index.html','../howto/index.html'];
  $('head').append('<link rel="stylesheet" href="../file.css">');
}

var k0={}
var k1={}

if (here0=='home'){
  var o0=[];
  var o1=[];
}else if (here0=='OOFe'){
  var o0=['about', 'requirements','tutorial','download'];
  var o1=['about.html', 'requirements.html','tutorial.html','download.html'];
}else if (here0=='Okean'){
  var o0=['about','overview','download'];
  var o1=['about.html', 'overview.html','download.html'];
}else if (here0=='How to'){
  var o0=['about','model grid','surface forcing','model inputs','misc','etc'];
  var o1=['about.html','grid_gen.html','interim.html','clm2ini.html','spec_plots_misc.html','etc_TODO.html'];

  k0['about']=[];
  k0['model grid']=['grid generation','edit mask','make a plot','extract coastline','extract bna'];
  k0['surface forcing']=['ERA Interim','GFS'];
  k0['model inputs']=['clm to ini','clm to bry','ini/clm/bry','surface','rivers'];
  k0['misc']=['specialized plots','etc'];
  k0['etc']=['etc'];

  k1['about']=[];
  k1['model grid']=['grid_gen.html','grid_medit.html','grid_plot.html','coastline.html','bna.html'];
  k1['surface forcing']=['interim.html','gfs.html'];
  k1['model inputs']=['clm2ini.html','clm2bry.html','inp_prog_TODO.html','inp_atm_TODO.html','inp_rivers_TODO.html'];
  k1['misc']=['spec_plots_misc.html','misc_etc_TODO.html'];
  k1['etc']=['etc_TODO.html'];

  k0=k0[here1];
  k1=k1[here1];
}

var s=''
for (var i=0; i<m0.length; i++){
  if (here0==m0[i]){
    var ss=';background-color: #cccccc;';
    var ss2='';//;color:white;';
  }else{
    var ss=';background-color: #f5f5f5;';
    var ss2='';
  }

  s+='<div style="float:left; padding:2px; border:1px solid white'+ss+'"><a class="titles0" style="'+ss2+'" href="'+m1[i]+'">'+m0[i]+'</a></div>';
}
s+='(previously at pong.tamu.edu/~mma/py ... created around 2011)';
$('#top2').html(s);

var s=''
for (var i=0; i<o0.length; i++){
  if (here1==o0[i]){
    var ss=';background-color: #cccccc;';
    var ss2='';//;color:white;';
  }else{
    var ss=';background-color: #f5f5f5;';
    var ss2='';
  }

  s+='<div style="float:left; padding:2px; border:1px solid white'+ss+'"><a style="'+ss2+'" href="'+o1[i]+'">'+o0[i]+'</a></div>';
}
$('#top').html(s);

var s=''
for (var i=0; i<k0.length; i++){
  if (here2==k0[i]){
    var ss=';background-color: #cccccc;';
    var ss2='';//;color:white;';
  }else{
    var ss=';background-color: #f5f5f5;';
    var ss2='';
  }

  s+='<div style="float:left; padding:2px; border:1px solid white'+ss+'"><a style="'+ss2+'" href="'+k1[i]+'">'+k0[i]+'</a></div>';
}
$('#sub_top').html(s);




if (here0=='OOFe'){$('#top1').html('Operational Ocean Forecast Python Engine')}
else if (here0=='Okean') {$('#top1').html('Okean - tools ocean modelling and analysis')}
else if (here0=='How to') {$('#top1').html('')}
else {$('#top1').html('')}

