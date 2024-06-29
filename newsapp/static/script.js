document.addEventListener('DOMContentLoaded', () => {
    const tagButtons = document.querySelectorAll('.tag-button');
    const newsContainer = document.getElementById('news-container');
    let selectedTag = null;

    async function fetchNews(tag) {
        console.log(`Fetching news for tag: ${tag}`);
        const response = await fetch('/fetch_news', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ tag })
        });
        const data = await response.json();
        console.log(`Fetched news data: `, data);
        return data;
    }

    async function displayNews() {
        const tag = selectedTag;

        const newsArticles = await fetchNews(tag);

        newsContainer.innerHTML = '';

        for (const article of newsArticles) {
            const { title, description, url, image_url, category } = article;

            if (category.toLowerCase() === 'business') {  // Filter out non-business articles
                const newsCard = document.createElement('div');
                newsCard.classList.add('news-card');

                newsCard.innerHTML = `
                    <a href="${url}" target="_blank">
                        <img src="${image_url}" alt="News Image">
                        <div class="content">
                            <h2>${title}</h2>
                            <p>${description}</p>
                            <span class="category">${category}</span>
                        </div>
                    </a>
                `;

                newsContainer.appendChild(newsCard);
            }
        }
    }

    tagButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            tagButtons.forEach(btn => btn.classList.remove('active'));
            e.target.classList.add('active');
            selectedTag = e.target.getAttribute('data-tag');
            displayNews();
        });
    });

    displayNews(); // Initial load
});
