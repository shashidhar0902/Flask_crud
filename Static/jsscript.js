function showProperties(){
    var showpropid = document.getElementById("showprop");
    var obj = {
        name: "John",
        age: 30,
        city: "New York"
        };
        for (var prop in obj) {
            showpropid.append(prop + ": " + obj[prop] );
            }
            
            
            
}