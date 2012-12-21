(defun kid-sdcv-to-buffer ()
  (interactive)
  (let ((word (if mark-active
                  (buffer-substring-no-properties
                   (region-beginning) (region-end))
                (current-word nil t))))
    (setq word (read-string
                (format "Search the dictionary for (default %s): " word)
                nil nil word))
    (set-buffer (get-buffer-create " *sdcv*"))
    (buffer-disable-undo)
    (erase-buffer)
    (append-to-file (concat word " ") word "~/words-memoir.txt")
    (let ((process
           (start-process-shell-command "sdcv" " *sdcv*" "~/bin/mydict.bash" word)))
      (set-process-sentinel
       process
       (lambda (process signal)
         (when (memq (process-status process) '(exit signal))
           (unless (string= (buffer-name) " *sdcv*")
             ;;(split-window-horizontally)
             (switch-to-buffer-other-window " *sdcv*")
             (local-set-key (kbd "d") 'kid-sdcv-to-buffer)
             (local-set-key (kbd "q")
                            (lambda ()
                              (interactive)
                              (bury-buffer)
                              (unless
                                  (null (cdr (window-list)))
                                (delete-window)))))
           (goto-char (point-min))))))))