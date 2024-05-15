// // hall list
// const maleHall = [
//   ["SHH", "Saddam Hossain Hall"],
//   ["JPBSMRH", "Jatir Pita Bangabandhu Sheikh Mujibur Rahman Hall"],
//   ["SSH", "Saddam Hossain Hall"],
//   ["LSH", "Lalon Shah Hall"],
//   ["SRH", "Sheikh Russel Hall"]
// ];



// const femaleHall = [
//   "Khaleda Zia Hall",
//   "Deshratno Sheikh Hasina Hall",
//   "Bangamata Sheikh Fazilatunnesa Mujib Hall",
// ]




// subject list
const Dfields = [
  "Electrical and Electronic Engineering",
  "Applied Chemistry & Chemical Engineering",
  "Computer Science and Engineering",
  "Information and Communication Technology",
  "Biotechnology and Genetic Engineering",
  "Applied Nutrition and Food Technology",
  "Mathematics",
  "Statistics",
  "Biomedical Engineering",
  "Environmental Science and Geography",
  "Pharmacy"
];

  const DshortNames = [
    "eee",
    "acce",
    "cse",
    "ict",
    "btge",
    "anft",
    "math",
    "statistics",
    "bme",
    "esg",
    "pharmacy"
  ];

  const Afields = [
    " Al-Quran and Islamic Studies",
    "Dawah & Islamic Studies",
    "Al-Hadith & Islamic Studies	",
  ];

  const AshortNames = [
    "AQIS",
    "DIS",
    "AHIS",
  ];


  const Bfields = [
    "Economics",
    "Arabic Language and Literature",
    "Bengali",
    "Islamic History and Culture",
    "English",
    "Public Administration",
    "Law",
    "Al-Fiqh and Legal Studies",
    "Folklore Studies",
    "Political Science",
    "Law and Land Management",
    "Development Studies",
    "Social Welfare",
    "Fine Arts"
  ];

  const BshortNames = [
    "economics",
    "arabic",
    "bengali",
    "ihc",
    "english",
    "pubad",
    "law",
    "alfiqh",
    "folklore",
    "ps",
    "llm",
    "ds",
    "sw",
    "finearts"
  ];
  

  const Cfields = [
    "Accounting and Information Systems",
    "Management",
    "Finance and Banking",
    "Marketing",
    "Human Resource Management",
    "Tourism and Hospitality Management"
  ];

  const CshortNames = [
    "ais",
    "management",
    "finance",
    "marketing",
    "hrm",
    "thm"
  ];

  
  

function selectUnit() {

    const selectedValue = document.getElementById('unit_subject').value;
    const subjects = document.getElementById('subject')

    if(selectedValue=='D')
    {
      let htmlOptions = '';
      Dfields.forEach( (field, index) =>{
        htmlOptions += `<option value="${DshortNames[index]}">${Dfields[index]}</option>`;
      });
  
      subjects.innerHTML = htmlOptions;
    }

    else if(selectedValue=='A')
      {
        let htmlOptions = '';
        Afields.forEach( (field, index) =>{
          htmlOptions += `<option value="${AshortNames[index]}">${Afields[index]}</option>`;
        });
    
        subjects.innerHTML = htmlOptions;
      }

      else if(selectedValue=='B')
        {
          let htmlOptions = '';
          Bfields.forEach( (field, index) =>{
            htmlOptions += `<option value="${BshortNames[index]}">${Bfields[index]}</option>`;
          });
      
          subjects.innerHTML = htmlOptions;
        }

        else
          {
            let htmlOptions = '';
            Cfields.forEach( (field, index) =>{
              htmlOptions += `<option value="${CshortNames[index]}">${Cfields[index]}</option>`;
            });
        
            subjects.innerHTML = htmlOptions;
          }


 
}


// function SelectGender()
//         {

//             const maleHall = [
//                 ["SHH", "Saddam Hossain Hall"],
//                 ["JPBSMRH", "Jatir Pita Bangabandhu Sheikh Mujibur Rahman Hall"],
//                 ["SSH", "Saddam Hossain Hall"],
//                 ["LSH", "Lalon Shah Hall"],
//                 ["SRH", "Sheikh Russel Hall"]
//             ];



//                         const femaleHall = [
//                             ["KZH", "Khaleda Zia Hall"],
//                             ["DSHH", "Deshratno Sheikh Hasina Hall"],
//                             ["BSFMH", "Bangamata Sheikh Fazilatunnesa Mujib Hall"],
//                            ];




//                 const gender = document.getElementById('gender').value;
//                 const hallName = document.getElementById('hallname');

//                 if(gender=='male')
//                 {
//                     let xmlCode = '';
//                     maleHall.forEach(value => {
//                         xmlCode += `<option value=${value[0]}>${value[1]}</option>`
//                     })
//                     hallName.innerHTML = xmlCode;
//                 }

//                 else{

//                     let xmlCode = '';
//                     femaleHall.forEach(value => {
//                         xmlCode += `<option value=${value[0]}>${value[1]}</option>`
//                     })
//                     hallName.innerHTML = xmlCode;

//                 }

// }
