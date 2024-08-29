set -euxo pipefail

rm -rf inner.zip outer.zip package.json node_modules out-1 out-2

wget -q -O inner.zip https://github.com/getsentry/sentry-android-gradle-plugin/releases/download/4.3.0/sentry-android-gradle-plugin-4.3.0.zip
sha256sum --check <<< 'f20bc17f0459128ad89c6d17947b9e9dd7286eacd686c69beae90f9f9969081c  inner.zip'

zip outer.zip inner.zip

cat >t.mjs <<EOF
import unzipper from 'unzipper';

const archive = await unzipper.Open.file(process.argv[2]);
await archive.extract({path: process.argv[3], concurrency: 2});
EOF

npm install unzipper >& /dev/null

node t.mjs outer.zip out-1
node t.mjs out-1/inner.zip out-2
