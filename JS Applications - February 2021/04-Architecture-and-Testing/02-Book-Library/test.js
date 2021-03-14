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
        await page.click('#loadBooks');

        let value = await page.$eval('tbody', el => [...el.children].length)
        let oldValue = value;
        assert.equal(value > 0, true);

        await page.fill('#title', 'TestTitle');
        await page.fill('#author', 'TestAuthor');

        await page.click('#submitForm');
        await page.click('#loadBooks');

        value = await page.$eval('tbody', el => [...el.children].length)
        assert.equal(value > oldValue, true);
    });
    it('secondTest', async () => {
        await page.goto('http://localhost:3000');
        await page.click('#loadBooks');

        let oldValue = await page.$eval('tbody', el => [...el.children].length)
        await page.click('body > table:nth-child(4) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > button:nth-child(2)');

        page.on('dialog', (dialog) => {
            return dialog.accept();
        })
        // https://playwright.dev/docs/dialogs ...
        await page.click('#loadBooks');
        let newValue = await page.$eval('tbody', el => [...el.children].length);

        assert.isTrue(oldValue > newValue);
    });
    it('thirdTest', async () => {
        await page.goto('http://localhost:3000');
        await page.click('#loadBooks');

        await page.click('body > table:nth-child(4) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(3) > button:nth-child(1)');

        await page.fill('#editTitle', 'newTestTitle');
        await page.fill('#editAuthor', 'newTestAuthor');
        await page.click('#editButton');

        await page.click('#loadBooks');

        assert.equal(await page.$eval('body > table:nth-child(4) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1)', el => el.textContent)
        , 'newTestTitle');
    })
});