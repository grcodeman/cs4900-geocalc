/*
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
ctx.fillStyle = "#FF0000";
canvas.height = canvas.width;
ctx.transform(1, 0, 0, -1, 0, canvas.height);

let xMax = canvas.height;
let yMax = canvas.width;

let slope = 1.0;
let intercept = 0;

let xArray = [10, 100, 200, 300, 400, 490];
let yArray = [10, 100, 200, 300, 400, 490];


// Plot Line
ctx.moveTo(0, intercept);
ctx.lineTo(xMax, f(xMax));
ctx.strokeStyle = "black";
ctx.stroke();

// Plot Small Line
ctx.moveTo(200, 300);
ctx.lineTo(300, 200);
ctx.strokeStyle = "green";
ctx.stroke();

// Plot Points
ctx.fillStyle = "blue";
for (let i = 0; i < xArray.length; i++) {
    let x = xArray[i];
    let y = yArray[i];
    ctx.beginPath();
    ctx.ellipse(x, y, 3, 3, 0, 0, Math.PI * 2);
    ctx.fill();
}

// Plot Circle
ctx.fillStyle = "red";
ctx.beginPath();
ctx.ellipse(200, 300, 50, 50, 0, 0, Math.PI * 2);
ctx.fill();

ctx.fillStyle = "red";
ctx.beginPath();
ctx.ellipse(300, 200, 25, 25, 0, 0, Math.PI * 2);
ctx.fill();
ctx.closePath();
ctx.restore();



const x_arr = '{{ point_data.x }}';
const y_arr = '{{ point_data.y }}';

ctx.fillStyle = "blue";
for (let i = 0; i < x_arr.length; i++) {
    ctx.beginPath();
    ctx.ellipse(x_arr[i], y_arr[i], 3, 3, 0, 0, MATH.PI * 2);
    ctx.fill();
}
*/

function f(x) {
    return x * slope + intercept;
}

function func(vars) {
    return vars
}

function draw_canvas(vars) {
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "#FF0000";
    canvas.height = canvas.width;
    ctx.transform(1, 0, 0, -1, 0, canvas.height);

    let xMax = canvas.height;
    let yMax = canvas.width;

    // Draw points from vars
    x_arr = vars.x;
    y_arr = vars.y;

    console.log(x_arr);
    console.log(y_arr);

    ctx.fillStyle = "blue";
    for (let i = 0; i < x_arr.length; i++) {
        ctx.beginPath();
        ctx.ellipse(x_arr[i], y_arr[i], 3, 3, 0, 0, Math.PI * 2);
        ctx.fill();
    }
}