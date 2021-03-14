const {assert} = require('chai');
const {chromium} = require('playwright-chromium');


let browser, page

describe('E2E tests', function() {
    before(async () => browser = await chromium.launch());
    after(async () => await browser.close());
    beforeEach(async () => page = await browser.newPage());
    afterEach(async () => await page.close());

    it('firstTest', async () => {
        await page.goto('http://localhost:3000');
        await page.click('#refresh');

        const value = await page.$eval('#messages', el => el.value);
        assert.equal(value.split('\n')[0], 'Spami: Hello, are you there?');
    });
    it('secondTest', async () => {
        await page.goto('http://localhost:3000');
        await page.fill('#author', 'TestAuthor');
        await page.fill('#content', 'TestContent');

        await page.click('#submit');

        await page.click('#refresh');
        const value = await page.$eval('#messages', el => el.value);
        assert.equal(value.split('\n').slice(-2).join(''), 'TestAuthor: TestContent: ');
    })
});