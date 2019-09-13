<!--<a href="http://fvcproductions.com"><img src="https://avatars1.githubusercontent.com/u/4284691?v=3&s=200" title="FVCproductions" alt="FVCproductions"></a>-->

[![CryoSec](https://raw.githubusercontent.com/DevManTillis/CryoSec/dev/files/cryosec_logo1.png)](http://tillisautomation.com)

<!--***CryoSec - System & Application Hardening Automation***-->

# CryoSec

> AWS cloud based system & application hardening automation simplified.

<!-- > ideally one sentence -->

<!-- > include terms/tags that can be searched -->

<!-- **Badges will go here** -->
<!--
- build status
- issues (waffle.io maybe)
- devDependencies
- npm package
- coverage
- slack
- downloads
- gitter chat
- license
- etc.

-->
<!--
[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![Dependency Status](http://img.shields.io/gemnasium/badges/badgerbadgerbadger.svg?style=flat-square)](https://gemnasium.com/badges/badgerbadgerbadger) [![Coverage Status](http://img.shields.io/coveralls/badges/badgerbadgerbadger.svg?style=flat-square)](https://coveralls.io/r/badges/badgerbadgerbadger) [![Code Climate](http://img.shields.io/codeclimate/github/badges/badgerbadgerbadger.svg?style=flat-square)](https://codeclimate.com/github/badges/badgerbadgerbadger) [![Github Issues](http://githubbadges.herokuapp.com/badges/badgerbadgerbadger/issues.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger/issues) [![Pending Pull-Requests](http://githubbadges.herokuapp.com/badges/badgerbadgerbadger/pulls.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger/pulls) [![Gem Version](http://img.shields.io/gem/v/badgerbadgerbadger.svg?style=flat-square)](https://rubygems.org/gems/badgerbadgerbadger)
- For more on these wonderful ~~badgers~~ badges, refer to <a href="http://badges.github.io/badgerbadgerbadger/" target="_blank">`badgerbadgerbadger`</a>.
-->
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org) [![Badges](http://img.shields.io/:badges-9/9-ff6799.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger)&nbsp;&nbsp;



<!-- ***Iteration One Planning*** -->

[![INSERT YOUR GRAPHIC HERE](https://raw.githubusercontent.com/DevManTillis/CryoSec/dev/files/Planning_Iteration_1.png)]()

<!--[![INSERT YOUR GRAPHIC HERE](http://i.imgur.com/dt8AUb6.png)]()-->
<!--
- Most people will glance at your `README`, *maybe* star it, and leave
- Ergo, people should understand instantly what your project is about based on your repo
-->

<!--
> Tips

- HAVE WHITE SPACE
- MAKE IT PRETTY
- GIFS ARE REALLY COOL

> GIF Tools
-->
<!--
- Use <a href="http://recordit.co/" target="_blank">**Recordit**</a> to create quicks screencasts of your desktop and export them as `GIF`s.
- For terminal sessions, there's <a href="https://github.com/chjj/ttystudio" target="_blank">**ttystudio**</a> which also supports exporting `GIF`s.
-->
<!--
**Recordit**

![Recordit GIF](http://g.recordit.co/iLN6A0vSD8.gif)

**ttystudio**

![ttystudio GIF](https://raw.githubusercontent.com/chjj/ttystudio/master/img/example.gif)
-->
---

## Table of Contents <!--(Optional)-->

<!-- > If you're `README` has a lot of info, section headers might be nice. -->

- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)
<!-- - [Team](#team) -->


---

## Example
<!--
```javascript
// code away!

let generateProject = project => {
  let code = [];
  for (let js = 0; js < project.length; js++) {
    code.push(js);
  }
};
```
-->

```bash
# Modify vulnerabilty item status via REST web request
cd microservices/vulndb

# Create AWS Cloudformation CryoSec stack
./stack create

# Test the CryoSec stack & recieve response from created API
./stack test

# Tear Down Resources
./stack delete
```

---

## Installation

- Setup a RedHat based system with atleast 4GB RAM and 2 vCPUs
- Install the AWS SAM Cli
[AWS SAM Cli Install Directions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-linux.html)
- Install Docker Community Edition
[Docker-CE Install directions]()

### Clone

- Clone this repo to your local machine using `https://github.com/DevManTillis/CryoSec`

### Setup

```shell
# Modify vulnerabilty item status via web request
$ aws configure
$ cd CryoSec/microservices/vulndb
$ ./stack create

# Generate a checklist via web request
$ cd CryoSec/microservices/genckl
$ ./stack create
```

---

<!--
## Features
## Usage (Optional)
## Documentation (Optional)
-->
## Tests (Optional)

```shell
$ aws configure
$ cd CryoSec/microservices/vulndb
$ ./stack test
```

---

## Contributing

> To get started...

### Step 1

- 🍴 Fork this repo!

- 👯 Clone this repo to your local machinee

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/jDevManTillis/compare" target="_blank">`https://github.com/DevManTillis/compare/`</a>.

---

<!-- ## Team -->

<!-- > Or Contributors/People -->
<!--
| <a href="http://fvcproductions.com" target="_blank">**Founder & DevSecOps Architect**</a> | <a href="http://fvcproductions.com" target="_blank">**Python Developer**</a> |
| :---: |:---: |
| [![devmantillis](https://avatars2.githubusercontent.com/u/15160643?s=200&v=4)](http://github.com/DevManTillis)    | [![nbatlle](https://raw.githubusercontent.com/DevManTillis/CryoSec/dev/files/nbatlle.png?s=200)](http://github.com/nbatlle) |
| <a href="http://github.com/DevManTillis" target="_blank">`github.com/DevManTillis`</a> | <a href="http://github.com/nbatlle" target="_blank">`github.com/nbatlle`</a> |
-->
<!--

| [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com)    | [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com) | [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com)  |
| <a href="http://github.com/fvcproductions" target="_blank">`github.com/fvcproductions`</a> | <a href="http://github.com/fvcproductions" target="_blank">`github.com/fvcproductions`</a> | <a href="http://github.com/fvcproductions" target="_blank">`github.com/fvcproductions`</a> |

- You can just grab their GitHub profile image URL
- You should probably resize their picture using `?s=200` at the end of the image URL.

---
-->
## FAQ

- **How do I do *specifically* so and so?**
    - No problem! Just do this.

---

## Support

Reach out to me at one of the following places!

- Website <a href="http://tillisautomation.com" target="_blank">`tillisautomation.com`</a>
- Email <a href="http://tillisautomation.com" target="_blank">`info@tillisautomation.com`</a>
<!-- - Twitter at <a href="http://twitter.com/fvcproductions" target="_blank">`@fvcproductions`</a>-->
<!-- - Insert more social links here.-->

---
<!--
## Donations (Optional)

- You could include a <a href="https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png" target="_blank">Gratipay</a> link as well.

[![Support via Gratipay](https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png)](https://gratipay.com/fvcproductions/)
-->

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
