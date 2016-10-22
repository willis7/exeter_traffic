node {
   stage 'setup'

      // Download the miniconda tool
      sh 'curl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh'

      // Make the tool executable
      sh 'chmod +x ./miniconda.sh'

      // Run setup
      sh './miniconda.sh -b -p /miniconda'

      // Make conda available on the command line
      env.PATH = "/miniconda/bin:${env.PATH}"

      // Test that coda is configured correctly
      sh 'conda info'

      // Get the latest code
      checkout scm

      // Setup conda
      sh 'hash -r'
      sh 'conda config --set always_yes yes --set changeps1 no'
      sh 'conda update -q conda'
      sh 'conda info -a'

   stage 'build'
      sh 'conda env create -f environment.yml'
      sh '''. activate exeter_traffic
            python scripts/make_relative_csv.py'''

   stage 'lint'
      sh "conda create -q -n test-environment python=${PYTHON_VERSION} pylint"
      sh '''. activate test-environment
            pylint scripts'''
}
