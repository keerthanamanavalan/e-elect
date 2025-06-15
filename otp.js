function send(){
    console.log("shiit only")
    const serviceID = "service_rp4li2a";
    const temp = "template_d8wa4rj"
    var params = {
      to_email : "wisdomwisdom846@gmail.com"
    }

    emailjs.send(serviceID,temp,params).then((res)=>{
        console.log(res)
    });
}