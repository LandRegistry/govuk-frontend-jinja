const nunjucks = require('nunjucks');
const ent = require('ent');
const prettyhtml = require('@starptech/prettyhtml');
const HtmlDiffer = require('@markedjs/html-differ').HtmlDiffer;
const examples = require('../../.cache/govuk-frontend-examples/all.json');
const glob = require('glob');
const path = require('path');

const htmlDiffer = new HtmlDiffer({
  ignoreAttributes: [
  ],
  ignoreSelfClosingSlash: true,
});

function cleanHtml(dirtyHtml) {
  return prettyhtml(ent.decode(dirtyHtml), {
    sortAttributes: true,
  }).contents;
}

// Grab list of components from govuk-frontend
const govukComponentPath = path.join(path.dirname(require.resolve('govuk-frontend/package.json')), 'govuk/components')
const components = glob.sync(path.join(govukComponentPath, '**/macro.njk')).map(componentPath => path.relative(govukComponentPath, path.dirname(componentPath)));

function diffComponentAgainstReferenceNunjucks(
  renderCallback
) {
  components.forEach(component => {
    describe(component, () => {
      examples[component].examples.forEach((example) => {
        describe(`${example.name}`, () => {
          it('output matches Nunjucks output', (done) => {
            const expected = cleanHtml(
              nunjucks.render(
                require.resolve(
                  `govuk-frontend/govuk/components/${component}/template.njk`
                ),
                {
                  params: example.data,
                }
              )
            );

            const actual = cleanHtml(renderCallback(component, example.data));

            // Make the actual comparison
            htmlDiffer.isEqual(actual, expected).then((comparison) => {
              // If the comparison is false, then compare the strings so
              // that the person can eyeball the diff
              if (!comparison) {
                // console.log('------------------------------------------')
                // console.log(htmlDiffer.diffHtml(expected, actual))
                expect(actual).toBe(expected);
              }

              expect(comparison).toBe(true);

              done();
            });
          });
        });
      });
    });
  });
}

module.exports = diffComponentAgainstReferenceNunjucks;
