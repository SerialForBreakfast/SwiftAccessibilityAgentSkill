require 'xcodeproj'
dir = ARGV.fetch(0)
Dir.chdir(dir) do
  mod, platform, deployment, resource = ARGV.drop(1)
  # Only derived build products are shared across sequential cells on one platform.
  # Each cell retains its own sources, intent, proof, first log and result bundle.
  cache = File.join(File.dirname(dir), "derived-#{platform}")
  Dir.mkdir(cache) unless File.directory?(cache)
  File.symlink(cache, 'dd') unless File.exist?('dd')
  project = Xcodeproj::Project.new('Batch.xcodeproj')
  fw = project.new_target(:framework, mod, platform.to_sym, deployment)
  test = project.new_target(:unit_test_bundle, 'Proof', platform.to_sym, deployment)
  test.add_dependency(fw)
  test.frameworks_build_phase.add_file_reference(fw.product_reference)
  [[fw, 'Subject'], [test, 'Tests']].each do |target, folder|
    Dir["#{folder}/*.swift"].each { |f| target.source_build_phase.add_file_reference(project.main_group.new_file(f)) }
    target.build_configurations.each do |cfg|
      cfg.build_settings.merge!({'GENERATE_INFOPLIST_FILE'=>'YES','ENABLE_TESTABILITY'=>'YES','SWIFT_VERSION'=>'5.0','CODE_SIGNING_ALLOWED'=>'NO','PRODUCT_BUNDLE_IDENTIFIER'=>"org.local.replay.#{target.name}",'SWIFT_EMIT_LOC_STRINGS'=>'NO'})
      cfg.build_settings['CLANG_MODULE_CACHE_PATH'] = File.join(File.dirname(dir), 'module-cache')
      cfg.build_settings['SWIFT_MODULE_CACHE_PATH'] = File.join(File.dirname(dir), 'module-cache')
    end
  end
  unless resource.nil?
    test.resources_build_phase.add_file_reference(project.main_group.new_file(resource))
  end
  scheme=Xcodeproj::XCScheme.new
  scheme.add_build_target(fw); scheme.add_test_target(test)
  scheme.save_as(project.path,'Replay',true)
  project.save
end
