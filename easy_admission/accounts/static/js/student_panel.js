

function UnitSelection()
{
    console.log("yes call")
    const unit = document.getElementById('units_selections').value 
    const section = document.getElementById('student_toggle_unit');
    
    if(unit=="B")
        {
            let xmlCode = ` 
            <ul class="nav d-block nav-pills">
            <li class="nav-item"><a  data-bs-toggle="pill" class="border nav-link active"  href="#Unit-select">Unit Select</a></li>
            <li class="nav-item"><a   class="border nav-link "  href="http://127.0.0.1:8000/information/make/application/condition/B">B-Unit Application </a></li>
            <li class="nav-item"><a   class="border nav-link "  href="http://127.0.0.1:8000/information/make/Prospectus/B">B-Unit Prospectus </a></li>
            <li class="nav-item"><a   class="border nav-link"  href="http://127.0.0.1:8000/information/make/Notice/B">B-Unit Notices</a></li>
            <li class="nav-item"><a   class="border nav-link"  href="#admit-card">B Unit Admit Card</a></li>
            </ul>
            `

            section.innerHTML = xmlCode;
        }

       else if(unit=="A")
            {
                let xmlCode = `
                
                <ul class="nav d-block nav-pills">
                <li class="nav-item"><a  data-bs-toggle="pill" class="border nav-link active"  href="#Unit-select">Unit Select</a></li>
                <li class="nav-item"><a   class="border nav-link "  href="http://127.0.0.1:8000/information/make/application/condition/A">A-Unit Application </a></li>
                <li class="nav-item"><a   class="border nav-link"  href="http://127.0.0.1:8000/information/make/Prospectus/A">A-Unit Prospectus</a></li>
                <li class="nav-item"><a   class="border nav-link"  href="http://127.0.0.1:8000/information/make/Notice/A">A-Unit Notices</a></li>
                <li class="nav-item"><a   class="border nav-link"  href="#admit-card">A Unit Admit Card</a></li>
             </ul>
                
                `
    
                section.innerHTML = xmlCode;
            }
        
            else if(unit=="C")
                {
                    let xmlCode = `
                    
                    <ul class="nav d-block nav-pills">
                    <li class="nav-item"><a  data-bs-toggle="pill" class="border nav-link active"  href="#Unit-select">Unit Select</a></li>
                    <li class="nav-item"><a   class="border nav-link "  href="http://127.0.0.1:8000/information/make/application/condition/C">C-Unit Application </a></li>
                    <li class="nav-item"><a   class="border nav-link"  href="http://127.0.0.1:8000/information/make/Prospectus/C">C-Unit Prospectus</a></li>
                    <li class="nav-item"><a   class="border nav-link"  href="http://127.0.0.1:8000/information/make/Notice/C">C-Unit Notices</a></li>
                    <li class="nav-item"><a   class="border nav-link"  href="#admit-card">C Unit Admit Card</a></li>
                 </ul>
                         `
                    section.innerHTML = xmlCode;
                }

            else

            if(unit=="D")
                {
                    let xmlCode = `
                    
                    <ul class="nav d-block nav-pills">
                    <li class="nav-item"><a  data-bs-toggle="pill" class="border nav-link active"  href="#Unit-select">Unit Select</a></li>
                    <li class="nav-item"><a class="border nav-link "  href="http://127.0.0.1:8000/information/make/application/condition/D">D-Unit Application </a></li>
                    <li class="nav-item"><a class="border nav-link"  href="http://127.0.0.1:8000/information/make/Prospectus/D">D-Unit Prospectus</a></li>
                    <li class="nav-item"><a class="border nav-link"  href="http://127.0.0.1:8000/information/make/Notice/D">D-Unit Notices</a></li>
                    <li class="nav-item"><a class="border nav-link"  href="#admit-card">D Unit Admit Card</a></li>
                 </ul>
                    
                    `
        
                    section.innerHTML = xmlCode;
                }
}