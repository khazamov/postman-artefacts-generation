# postman-artefacts-generation

## Introduction

Postman is a de-facto standard tool for testing and exploring the APIs in accordance to the API-first principles. Postman can store and manage API specifications, documentation, workflow recipes, test cases and results, metrics, and everything else related to APIs.
This workflow generates Postman collections based on the Criteo Public API Open API specifications.

## Audience

This README document is intended for Criteo internal users. 
If you are a Criteo client and would to explore Criteo on Postman please checkout the following guide https://developers.criteo.com/marketing-solutions/docs/use-postman-with-the-criteo-marketing-solutions-api

## Requirements

In order to successfully run the workflow you will need to setup workspace identifiers: 
* POSTMAN_WORKSPACE_ID 
* POSTMAN_PREPROD_WORKSPACE_ID
* POSTMAN_MANAGEMENT

They can be setup under Security -> Secret -> Actions.

Once the script has been ran update the collections with the pre-request scripts for automatic token management.

## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
