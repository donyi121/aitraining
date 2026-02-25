async function predict() {
    const data = {
        size: parseFloat(document.getElementById("size").value),
        bhk: parseInt(document.getElementById("bhk").value),
        location: parseFloat(document.getElementById("location").value),
        price_cr: parseFloat(document.getElementById("price").value)
    };

    const res = await fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await res.json();

    document.getElementById("result").innerText =
        "Predicted Segment: " + result.segment;

    const img = document.getElementById("posterImg");
    img.src = result.poster;
    img.style.display = "block";
}