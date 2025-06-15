const fileSelector = document.querySelector('input')
const start = document.querySelector('button')
const voters = ['715523104013']
const nums = '1234567890'
let roll = ''
function show(){
    const rec = new Tesseract.TesseractWorker()
    rec.recognize(fileSelector.files[0])
        .progress(function (response){
            console.log(response);
        })
        .then(function (data){
            console.log(data.text)
            for(let i=1;i<data.text.length;i++){
                
                if(nums.includes(data.text[i]) && (roll.length<12)){
                    roll+=data.text[i]
                }
            }
            console.log(roll)
            if(voters.includes(roll)){
                console.log("Voted already")
            }else{
                console.log("Not yet voted")
        
            }
        })
    
}
