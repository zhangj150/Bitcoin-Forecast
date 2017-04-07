function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

function filterFunction() {
    var input, filter, dropdownVal, a;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    dropdownVal = document.getElementById("myDropdown");
    a = dropdownVal.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        if (a[i].innerHTML.toUpperCase().indexOf(filter) != -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }



}