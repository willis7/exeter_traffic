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

   stage 'conda bootstrap'

      // Set the run environment
      sh 'conda env create -f environment.yml'
      sh 'source activate exeter_traffic'

   stage 'lint'

      sh 'pylint scripts/'
}
