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

function draw_canvas(points, lines, circles) {
    // Setup 2d canvas
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "#FF0000";
    canvas.height = canvas.width;
    ctx.transform(1, 0, 0, -1, 0, canvas.height);

    let xMax = canvas.height;
    let yMax = canvas.width;

    // Draw lines
    var start_x_arr = lines.start_x;
    var start_y_arr = lines.start_y;
    var end_x_arr = lines.end_x;
    var end_y_arr = lines.end_y;

    for (let i = 0; i < start_x_arr.length; i++) {
        ctx.moveTo(start_x_arr[i], start_y_arr[i]);
        ctx.lineTo(end_x_arr[i], end_y_arr[i]);
        ctx.strokeStyle = "black";
        ctx.stroke();
    }

    // Draw points
    var x_arr = points.x;
    var y_arr = points.y;

    console.log(x_arr);
    console.log(y_arr);

    ctx.fillStyle = "blue";
    for (let i = 0; i < x_arr.length; i++) {
        ctx.beginPath();
        ctx.ellipse(x_arr[i], y_arr[i], 3, 3, 0, 0, Math.PI * 2);
        ctx.fill();
    }

    // Draw circles
    var center_x_arr = circles.x;
    var center_y_arr = circles.y;
    var radius_arr = circles.radius;

    ctx.fillStyle = "red";
    for (let i = 0; i < center_x_arr.length; i++) {
        ctx.beginPath();
        ctx.ellipse(center_x_arr[i], center_y_arr[i], radius_arr[i], radius_arr[i], 0, 0, Math.PI * 2);
        ctx.fill();
    }

}