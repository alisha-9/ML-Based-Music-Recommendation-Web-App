document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("recommendForm");
    const resultsContainer = document.getElementById("results");
    const loadingIndicator = document.getElementById("loading");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        // Get input values
        const songTitle = document.getElementById("song_title").value;
        const genre = document.getElementById("genre").value;
        const artist = document.getElementById("artist").value;
        const topN = parseInt(document.getElementById("top_n").value) || 5;

        // Payload for API
        const payload = {
            song_title: songTitle || null,
            genre: genre || null,
            artist: artist || null,
            top_n: topN
        };

        // Show loading
        loadingIndicator.style.display = "block";
        resultsContainer.innerHTML = "";

        try {
            const response = await fetch("/recommend", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const data = await response.json();
            loadingIndicator.style.display = "none";

            if (data.recommendations && data.recommendations.length > 0) {
                data.recommendations.forEach((rec) => {
                    const card = document.createElement("div");
                    card.classList.add("song-card");
                    card.innerHTML = `
                        <strong>${rec.name}</strong><br>
                        <small>${rec.artists}</small><br>
                        <em>${rec.genre || ""}</em>
                    `;
                    resultsContainer.appendChild(card);
                });
            } else {
                resultsContainer.innerHTML = "<p>No recommendations found.</p>";
            }
        } catch (error) {
            console.error("Error:", error);
            loadingIndicator.style.display = "none";
            resultsContainer.innerHTML = "<p>Something went wrong. Try again later.</p>";
        }
    });
});
