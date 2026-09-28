const { chromium } = require('playwright');

const CHROME_PATH = '/run/current-system/sw/bin/google-chrome';
const BASE_URL = 'http://localhost:8080';

const pages = ['/', '/about.html', '/products.html'];

function randomItem(array) {
    return array[Math.floor(Math.random() * array.length)];
}

function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

async function main() {
    const browser = await chromium.launch({
        headless: true,
        executablePath: CHROME_PATH
    });

    const VISITORS = 30;

    for (let i = 1; i <= VISITORS; i++) {
        // New context = new visitor/cookie jar
        const context = await browser.newContext();

        const page = await context.newPage();

        console.log(`Visitor ${i}/${VISITORS}`);

        // First page
        await page.goto(BASE_URL + '/', {
            waitUntil: 'networkidle'
        });

        await sleep(1000 + Math.random() * 3000);

        // Random browsing behaviour
        const numberOfPages = 1 + Math.floor(Math.random() * 3);

        for (let j = 0; j < numberOfPages; j++) {
            const target = randomItem(pages);

            await page.goto(BASE_URL + target, {
                waitUntil: 'networkidle'
            });

            console.log(`  → ${target}`);

            await sleep(1000 + Math.random() * 4000);
        }

        await context.close();

        // Small gap between visitors
        await sleep(500 + Math.random() * 1500);
    }

    await browser.close();

    console.log('\nTraffic generation complete!');
}

main().catch(console.error);
