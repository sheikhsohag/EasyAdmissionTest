

function UnitSelection()
{
    const unit = document.getElementById('units_selections').value 
    const section = document.getElementById('student_toggle_unit');
    
    if(unit=="B")
        {
            let xmlCode = ` 
            <ul class="nav d-block nav-pills">
            <li class="nav-item"><a  data-bs-toggle="pill" class="border nav-link active"  href="#Unit-select">Unit Select</a></li>
            <li class="nav-item"><a   class="border nav-link "  href="{% url 'application_condition' %}">B-Unit Application </a></li>
            <li class="nav-item"><a   class="border nav-link "  href="{% url 'prospectus' %}">B-Unit Prospectus </a></li>
            <li class="nav-item"><a   class="border nav-link"  href="{% url 'notice' %}">B-Unit Notices</a></li>
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
                <li class="nav-item"><a   class="border nav-link "  href="{% url 'application_condition' %}">A-Unit Application </a></li>
                <li class="nav-item"><a   class="border nav-link"  href="{% url 'prospectus' %}">A-Unit Prospectus</a></li>
                <li class="nav-item"><a   class="border nav-link"  href="{% url 'notice' %}">A-Unit Notices</a></li>
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
                    <li class="nav-item"><a   class="border nav-link "  href="{% url 'application_condition' %}">C-Unit Application </a></li>
                    <li class="nav-item"><a   class="border nav-link"  href="{% url 'prospectus' %}">C-Unit Prospectus</a></li>
                    <li class="nav-item"><a   class="border nav-link"  href="{% url 'notice' %}">C-Unit Notices</a></li>
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
                    <li class="nav-item"><a class="border nav-link "  href="{% url 'application_condition' %}">D-Unit Application </a></li>
                    <li class="nav-item"><a class="border nav-link"  href="{% url 'prospectus' %}">D-Unit Prospectus</a></li>
                    <li class="nav-item"><a class="border nav-link"  href="{% url 'notice' %}">D-Unit Notices</a></li>
                    <li class="nav-item"><a class="border nav-link"  href="#admit-card">D Unit Admit Card</a></li>
                 </ul>
                    
                    `
        
                    section.innerHTML = xmlCode;
                }
}