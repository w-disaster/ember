## [1.2.3](https://github.com/w-disaster/ember/compare/1.2.2...1.2.3) (2025-04-28)

### Bug Fixes

* raw feature extraction order ([4c76f3e](https://github.com/w-disaster/ember/commit/4c76f3ef57115b550b5aa9bd23846daba47e3eec))

## [1.2.2](https://github.com/w-disaster/ember/compare/1.2.1...1.2.2) (2025-04-27)

### Bug Fixes

* dataset filename in test script ([3ec3e13](https://github.com/w-disaster/ember/commit/3ec3e136cdbc051fceef4c65955adf894f5bea99))

### Tests

* add dataset shape test ([0a9ec06](https://github.com/w-disaster/ember/commit/0a9ec0697837de2e779d7ebfca5487795a7e8270))

### Build and continuous integration

* add test setup workflow ([b4fbbff](https://github.com/w-disaster/ember/commit/b4fbbffaaafa80bd6e1b223cf5065216f6bc860c))

### General maintenance

* remove pycache dir ([1f6fc76](https://github.com/w-disaster/ember/commit/1f6fc7696404f26b9848ca0084f698d886900aa9))
* run tests only on linux ([17b3a7d](https://github.com/w-disaster/ember/commit/17b3a7d02f42884f1398a185940e31eedbc9d0e9))
* temporary disable test with coverage ([a52c419](https://github.com/w-disaster/ember/commit/a52c41914430463ba2b4a766fb562eafc026348e))

## [1.2.1](https://github.com/w-disaster/ember/compare/1.2.0...1.2.1) (2025-04-27)

### Dependency updates

* **deps:** update dependency poetry to v2 ([78aca9e](https://github.com/w-disaster/ember/commit/78aca9e6739427c870f9bb12c1f66fdd7f0f30b5))

### Bug Fixes

* **deps:** update dependency numpy to v2 ([30ec109](https://github.com/w-disaster/ember/commit/30ec10950d33ff8bb4c3cb3831b8a4abbd06e25c))

### General maintenance

* remove unused dirs ([7caa048](https://github.com/w-disaster/ember/commit/7caa048b82cd9071fc718b3f2a3cb0edc6afc33d))

## [1.2.0](https://github.com/w-disaster/ember/compare/1.1.0...1.2.0) (2025-04-27)

### Features

* add family column in final dataset ([58463a6](https://github.com/w-disaster/ember/commit/58463a6a6781fc219e28d3b8c1136cef0baccb69))

## [1.1.0](https://github.com/w-disaster/ember/compare/1.0.0...1.1.0) (2025-04-26)

### Features

* feature extraction through docker ([fbeb9ed](https://github.com/w-disaster/ember/commit/fbeb9ede7d23434db753758eae885e5690a4994c))

### Dependency updates

* **deps:** update docker/build-push-action digest to 14487ce ([881dd7d](https://github.com/w-disaster/ember/commit/881dd7dc978e52f303a1d85b782988265a4db1af))

### Build and continuous integration

* restore old docker image deploy ([75bae35](https://github.com/w-disaster/ember/commit/75bae35ca049d2cff0054f6092cba4cab95d53d8))
* trigger deploy-image on master ([8dc4348](https://github.com/w-disaster/ember/commit/8dc4348c57e7d14a3e4f000a1bac08de3f266f5c))
* update deploy image ci file ([0dadc25](https://github.com/w-disaster/ember/commit/0dadc2591805b9c7341149301b7ba94b23d840fe))

### General maintenance

* naive Dockerfile ([8de000c](https://github.com/w-disaster/ember/commit/8de000c5753dc890086d0463cf0575f59b308c30))
* remove setup.py ([f9131ee](https://github.com/w-disaster/ember/commit/f9131eea7ebd2dfeb51808cf588c0eb28f072684))
* remove useless requirements ([352db3a](https://github.com/w-disaster/ember/commit/352db3aade02901e555bc14e647c55273d8a729d))

## 1.0.0 (2025-04-26)

### Features

* feature extraction using notebook ([f96a59d](https://github.com/w-disaster/ember/commit/f96a59dd3813260102bbbe2cd892a33a62409bb4))

### Bug Fixes

* other ruff check errors ([9ec0eed](https://github.com/w-disaster/ember/commit/9ec0eed324e0ba79c71146c248c5f908b9b8a1ce))
* static checks errors ([2bd3f12](https://github.com/w-disaster/ember/commit/2bd3f12f4d58bcf1a3665eb8a493ef923396941a))

### Build and continuous integration

* add package publish ([280427b](https://github.com/w-disaster/ember/commit/280427b8478509d33e9dc53ab6b8d63483a20bcc))
* disable pypi release ([c69d4db](https://github.com/w-disaster/ember/commit/c69d4db0daa98266bd2f6ec1f432de67449a427a))
* restore poetry pypi publish ([b873e8b](https://github.com/w-disaster/ember/commit/b873e8b20f3a0ee0095f619cc60ba8e9e351b54d))
* use github token ([847a23f](https://github.com/w-disaster/ember/commit/847a23f7cd3564b4f00cb1541ef17aad7a3ea3ae))
* use GITHUB_TOKEN ([ed02837](https://github.com/w-disaster/ember/commit/ed02837fed7819abcf105c434862a53c9ca3c1b9))

### General maintenance

* add GH workflows ([4fe9ebe](https://github.com/w-disaster/ember/commit/4fe9ebe1d351d0562ebe70dc2e8bb98a04bf2dbd))
* add python template ([afb76e6](https://github.com/w-disaster/ember/commit/afb76e6b9546c9440fbc277febcf1f5a5bc1af8a))
* change project name ([b6f791b](https://github.com/w-disaster/ember/commit/b6f791bd3b2918bd870219530caa49ee0ef16e55))
* disable imports in tests ([285e4fe](https://github.com/w-disaster/ember/commit/285e4fe6c9d8bad3fab68a811ff9f4843982aec6))
* disable static checks ([181192f](https://github.com/w-disaster/ember/commit/181192f8ddb37c951ccc8318269c756ccaba903b))
* format code ([0d5cbe6](https://github.com/w-disaster/ember/commit/0d5cbe6be6aae9b2d78ec48206f8f34227e4a13f))
* **release:** 1.0.0 [skip ci] ([3bbd32e](https://github.com/w-disaster/ember/commit/3bbd32e6dba59c1bb9edb10b05865cc35448355f))
* **release:** 1.0.0 [skip ci] ([843dd17](https://github.com/w-disaster/ember/commit/843dd17646f63187b66957507676ea889482e0e2))
* **release:** 1.0.0 [skip ci] ([06a6114](https://github.com/w-disaster/ember/commit/06a61145698bf6c4d59889d301549cd7e2ac3c4a))
* **release:** 1.0.0 [skip ci] ([6521543](https://github.com/w-disaster/ember/commit/65215439d6e2bb39bb038801c4d9b49bd601cb58))
* **release:** 1.0.0 [skip ci] ([eb9c449](https://github.com/w-disaster/ember/commit/eb9c44975a5162083e3c08fb03bb58c4321a2d26))
* remove changelog ([9481c34](https://github.com/w-disaster/ember/commit/9481c346ad5700efca984639a363946f2697f15d))
* rm changelog ([3182282](https://github.com/w-disaster/ember/commit/318228265a40e258a7bce83bfa0b7be4a879433d))
* rm changelog ([9d5ba5e](https://github.com/w-disaster/ember/commit/9d5ba5ec33953d3023067e6dbcffab5717a1e5f8))
* trying to disable pypi publish ([171ebeb](https://github.com/w-disaster/ember/commit/171ebebe569100258de0c6e94ea27dc856f52356))
